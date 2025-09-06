; db -> define byte
; dw -> define word (16 bits)
; dd -> define double word (32 bits)
; dq -> define quad word (64 bits)

section .data
    fizz_msg db "fizz"
    buzz_msg db "buzz"
    fizz_len equ 4
    buzz_len equ 4

section .bss
    input_buf resb 20  ; Reserve 20 bytes for input
    num       resq 1   ; 64-bit integer

section .text
    global _start

_start:
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; START OF INPUT ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    ; read(0, input_buf, 20)
    mov rax, 0          ; syscall number for read
    mov rdi, 0          ; fd = stdin
    mov rsi, input_buf  ; buffer
    mov rdx, 20         ; size
    syscall
    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; END OF INPUT ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    ; Convert input string -> number (RAX will hold result)
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
    mov r12, rax          ; save original number in r12

    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; fizz check ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov rax, r12          ; load number
    mov rcx, 7
    xor rdx, rdx
    div rcx               ; rax = num / 7, rdx = num % 7

    cmp rdx, 5
    jne .skip_fizz
    mov rax, 1            ; syscall: write
    mov rdi, 1            ; fd = stdout
    mov rsi, fizz_msg
    mov rdx, fizz_len
    syscall
.skip_fizz:

    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; buzz check ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov rax, r12          ; restore number
    mov rcx, 2
    xor rdx, rdx
    div rcx               ; rax = num / 2, rdx = num % 2

    cmp rdx, 0
    jne .skip_buzz
    mov rax, 1            ; syscall: write
    mov rdi, 1
    mov rsi, buzz_msg
    mov rdx, buzz_len
    syscall
.skip_buzz:

    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; exit(0) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
    mov rax, 60           ; syscall: exit
    xor rdi, rdi          ; status = 0
    syscall
