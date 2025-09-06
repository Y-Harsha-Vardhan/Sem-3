section .data
    buffer  db 20 dup(0)     ; Output buffer for result string

section .bss
    input_buf resb 20  ; Reserve 20 bytes for input
    num     resq 1     ; 64-bit integer

section .text
    global _start ; essentially just means start here


_start:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; START OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; Take in number as input from user
    ; You can do this using read(0, input_buffer, size) syscall, syscall number for read is 0
    ; Make sure your input buffer is stored in rsi :)
    mov rax, 0
    mov rdi, 0
    mov rsi, input_buf
    mov rdx, 20
    syscall
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; END OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; The below code simply converts input string to a number, don't worry about it
    mov rsi, input_buf  ; rsi points to buffer
    xor rax, rax        ; accumulator = 0

.convert1:
    movzx rcx, byte [rsi] ; load byte
    cmp rcx, 10           ; check for newline
    je .done1
    sub rcx, '0'          ; convert ASCII to digit
    imul rax, rax, 10
    add rax, rcx
    inc rsi
    jmp .convert1

.done1:
    mov r12, rax
    ; Now RAX contains the number entered

    ; Implement following C code:
    ; int a = 0;
    ; int b = 1;
    ; for (int i=0; i < n; i++) {
    ;     int c = a + b;
    ;     a = b;
    ;     b = c;
    ; }
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; START OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov rax, r12 ;loading back the number into rax
    mov r13, 0   ; r13 = a
    mov r14, 1   ; r14 = b
    mov r15, 0   ; r15 = i

.forBegin:
    cmp r15, rax
    jge .forEnd

    mov rbx, r13 ; rbx = a
    add rbx, r14 ; rbx = a + b
    mov r13, r14 ; a = b
    mov r14, rbx ; b = rbx
    add r15, 1   ; i = i + 1
    jmp .forBegin

.forEnd:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; END OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; Print the result
    ; C code is:
    ; i = 19
    ; while (a > 0) {
    ;   buff[i] = a % 10 + '0'; Note you must access only the lower 8 bits of your register storing a here :) for example, for rdx, lower 8 bits are stored in dl
    ;   a /= 10;
    ;   i--;
    ; }
    ; write(1, buff + i + 1, 19 - i); 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; START OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov r15, 19 ; i = 19
    mov rax, r13; rax = n (to be printed)

.whileLoop:
    cmp rax, 0
    je .whileEnd

    xor rdx, rdx ; clearing rdx
    mov rcx, 10  ; rbx = 10
    div rcx      ; dividing rax by rbx, rax = quotient and rdx = remainder

    add dl, '0'  ; converting remainder into ASCII
    mov [buffer + r15], dl ; storing it in buffer[i]
    dec r15
    jmp .whileLoop

.whileEnd:
; printing the string in the terminal
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer + r15 + 1]
    mov rdx, 19
    sub rdx, r15
    syscall

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; END OF YOUR CODE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov rax, 60              ; syscall: exit
    xor rdi, rdi             ; exit code 0
    syscall
