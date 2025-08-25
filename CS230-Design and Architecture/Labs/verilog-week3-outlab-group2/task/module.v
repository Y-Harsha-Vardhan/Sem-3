module Encrypt(
    input  [63:0] plaintext,
    input  [63:0] secretKey,
    output [63:0] ciphertext
);
    wire [63:0] state[0:10];
    wire [63:0] roundKeys[0:10];

    assign roundKeys[0] = secretKey;

    AddRoundKey preRound (
        .currentState(plaintext),
        .roundKey(secretKey),
        .nextState(state[0])
    );

    genvar r;
    generate
        for (r = 1; r <= 10; r = r + 1) begin : rounds
            NextKey nk (
                .currentKey(roundKeys[r-1]),
                .nextKey(roundKeys[r])
            );

            Round round_inst (
                .currentState(state[r-1]),
                .roundKey(roundKeys[r]),
                .nextState(state[r])
            );
        end
    endgenerate

    assign ciphertext = state[10];

endmodule


module Round(
    input  [63:0] currentState,
    input  [63:0] roundKey,
    output [63:0] nextState
);
    wire [63:0] subBytesState;
    wire [63:0] shiftedState;

    genvar i;
    generate
        for (i = 0; i < 16; i = i + 1) begin : sbox_loop
            SBox s (
                .in(currentState[i*4 +: 4]),
                .out(subBytesState[i*4 +: 4])
            );
        end
    endgenerate

    ShiftRows sr (
        .currentState(subBytesState),
        .nextState(shiftedState)
    );

    AddRoundKey ark (
        .currentState(shiftedState),
        .roundKey(roundKey),
        .nextState(nextState)
    );

endmodule


module SBox(
    input [3:0]in ,
    output [3:0]out
);
    assign out[3] = (~in[3])&(~in[2])&(~in[1])&in[0] | (~in[3])&(~in[0])&(~in[1])&in[2] | (~in[0])&(~in[2])&(~in[1])&in[3] | in[3]&in[2]&in[0]&(~in[1]) | (~in[3])&in[2]&in[1] | in[3]&in[1]&in[0];
    assign out[2] = (~in[3])&(~in[1])&(~in[0]) | in[3]&in[2]&(~in[1]) | in[3]&in[1]&(~in[2]) | (~in[3])&(~in[2])&in[1]&in[0] | (~in[3])&(~in[0])&in[1]&in[2];
    assign out[1] = (~in[3])&(~in[1])&(~in[2]) | in[0]&in[2]&(~in[1]) | (~in[1])&(~in[2])&in[3] | (~in[3])&(~in[0])&in[1]&in[2] | (~in[2])&(~in[0])&in[1]&in[3];
    assign out[0] = (~in[0])&(~in[1])&(in[2]) | in[0]&(~in[3])&(~in[1]) | (in[1])&(in[2])&in[3] | (~in[3])&(~in[0])&in[1]&in[2] | (~in[2])&(~in[0])&in[1]&in[3];

endmodule

module NextKey(
    input  [63:0] currentKey,
    output [63:0] nextKey
);
    assign nextKey[63:0] = {currentKey[59:0], currentKey[63:60]}; 
endmodule

module ShiftRows(
    input  [63:0] currentState ,
    output [63:0] nextState    
);
    wire [3:0] b, a, x9, x8, x7, x6, x5, x4, x3, x2, x1, x0;
    assign b = currentState[19:16];
    assign a = currentState[23:20];
    assign x9 = currentState[27:24];
    assign x8 = currentState[31:28];
    assign x7 = currentState[35:32];
    assign x6 = currentState[39:36];
    assign x5 = currentState[43:40];
    assign x4 = currentState[47:44];
    assign x3 = currentState[51:48];
    assign x2 = currentState[55:52];
    assign x1 = currentState[59:56];
    assign x0 = currentState[63:60];
    assign nextState[15:0] = currentState[15:0];
    assign nextState[31:16] = {b, x8, x9, a};
    assign nextState[47:32] = {x6, x7, x4, x5};
    assign nextState[63:48] = {x1, x2, x3, x0};

endmodule

module AddRoundKey(
    input  [63:0] currentState ,
    input  [63:0] roundKey     ,
    output [63:0] nextState    
);
    assign nextState = currentState^roundKey;

endmodule
