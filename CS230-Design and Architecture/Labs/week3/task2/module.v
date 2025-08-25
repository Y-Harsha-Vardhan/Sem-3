module ShiftRows(
    input  [63:0] currentState ,
    output [63:0] nextState    
);
    // Fill shift row logic here
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