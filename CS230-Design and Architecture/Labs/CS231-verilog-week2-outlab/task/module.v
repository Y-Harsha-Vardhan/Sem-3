module getNextState (
    input  [2:0] currentState,
    output reg [2:0] nextState
);
    reg t0, t1, t2;

    always @(*) begin
        t0 = 1'b1;                         
        t1 = currentState[0];               
        t2 = currentState[1] & currentState[0]; 

        nextState[0] = currentState[0] ^ t0;
        nextState[1] = currentState[1] ^ t1;
        nextState[2] = currentState[2] ^ t2;

        if (currentState == 3'b111) begin
            nextState = 3'b001;
        end
    end
endmodule


module threeBitCounter (
    input clk,
    input reset,
    output reg [2:0] count
);
    wire [2:0] nextState;

    getNextState gns (
        .currentState(count),
        .nextState(nextState)
    );

    always @(posedge clk) begin
        if (reset)
            count <= 3'b000;
        else
            count <= nextState;
    end
endmodule


module counterToLights (
    input  [2:0] count,
    output [2:0] rgb
);
    wire a = count[2];  
    wire b = count[1];
    wire c = count[0];  

    assign rgb[2] = (~b & ~c) | ( c & (a ^ b));
    assign rgb[1] = (~a & ~b) | (~c & (a ^ b));
    assign rgb[0] = (~a & ~c) | ( a & (b ^ c));
endmodule


module rgbLighter (
    input clk,
    input reset,
    output [2:0] rgb
);
    wire [2:0] count;

    threeBitCounter counter_inst (
        .clk(clk),
        .reset(reset),
        .count(count)
    );

    counterToLights mapping_inst (
        .count(count),
        .rgb(rgb)
    );
endmodule
