section .data
    shifted_disk db "Shifted disk "
    from_str db " from "
    to_str db " to "
    a_rod db 'A'
    b_rod db 'B'
    c_rod db 'C'
    newline db 10
    shifted_len equ 13
    from_len equ 6
    to_len equ 4
    buffer db 100 dup(0) ; Output buffer for result string

section .bss
    input_buf resb 20  ; Reserve 20 bytes for input
    num resq 1         ; 64-bit integer

section .text
    global printNum
    global hanoi
    global _start 
    global printFromAndTo

printNum:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Start of your code ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Write code to print an arbitary number stored in rax
; rax = number to print
    mov rcx, 19         ; rcx = buffer index (filled from right)
    cmp rax, 0
    jne .numLoop

; If n = 0, then:
    mov byte [buffer + 19], '0'
    ; Printing the number
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer + 19] ; loading the address of '0'
    mov rdx, 1
    syscall
    ret

.numLoop:
    xor rdx, rdx         ; emptying rdx
    mov rbx, 10
    div rbx              ; quotient in rax, remainder in rdx
    add dl, '0'          ; converting remainder into ASCII 
    mov [buffer + rcx], dl
    dec rcx
    test rax, rax
    jnz .numLoop

; Printing the number:
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer + rcx + 1]   ; points to first digit
    mov rdx, 19
    sub rdx, rcx                  ; length = 19 - rcx
    syscall
    ret
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  End of your code  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

printFromAndTo:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Start of your code ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Write code to print " from " *rsi " to " *rdx
    mov r8b, sil            ; Saving 'from' and 'to' characters before rsi/rdx are overwritten
    mov r9b, dl            

; First printing " from "
    mov rax, 1
    mov rdi, 1
    mov rsi, from_str
    mov rdx, from_len
    syscall

; printing the *rsi (single char)
    mov byte [buffer], r8b
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer]
    mov rdx, 1
    syscall

; printing the " to "
    mov rax, 1
    mov rdi, 1
    mov rsi, to_str
    mov rdx, to_len
    syscall

; printing the *rdx
    mov byte [buffer], r9b
    mov rax, 1
    mov rdi, 1
    lea rsi, [buffer]
    mov rdx, 1
    syscall

; printing newline
    mov rax, 1
    mov rdi, 1
    mov rsi, newline
    mov rdx, 1
    syscall
    ret
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  End of your code  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

hanoi:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Start of your code ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;; C code for function
;;;; void hanoi(int n, char from, char to, char aux) {
;;;;     if (n == 1) {
;;;;         printf("Shifted disk 1 from %c to %c\n", from, to);
;;;;         return;
;;;;     }
;;;;     hanoi(n - 1, from, aux, to);
;;;;     printf("Shifted disk %d from %c to %c\n", n, from, to);
;;;;     hanoi(n - 1, aux, to, from);
;;;; }

; Arguments:
;   rdi = n
;   rsi = from
;   rdx = to
;   rcx = aux

    push r12
    push r13
    push r14
    push r15

    mov r12, rdi   ; r12 := n
    mov r13, rsi   ; r13 := from
    mov r14, rdx   ; r14 := to
    mov r15, rcx   ; r15 := aux

    cmp r12, 1
    jne .recurse

    ; base case when n == 1
    ; print "Shifted disk "
    mov rax, 1
    mov rdi, 1
    mov rsi, shifted_disk
    mov rdx, shifted_len
    syscall

    ; print the number 1
    mov rax, 1
    call printNum      

    ; print " from *rsi to *rdx\n"
    mov rsi, r13        ; from char
    mov rdx, r14        ; to char
    call printFromAndTo

    pop r15
    pop r14
    pop r13
    pop r12
    ret

.recurse:

    ; hanoi(n-1, from, aux, to)
    mov rdi, r12        ; rdi = n
    dec rdi             ; rdi = n-1
    mov rsi, r13        ; from
    mov rdx, r15        ; to = aux 
    mov rcx, r14        ; aux = original to
    call hanoi

    ; printing "Shifted disk n from from to to"
    mov rax, 1
    mov rdi, 1
    mov rsi, shifted_disk
    mov rdx, shifted_len
    syscall

    mov rax, r12        ; original n
    call printNum

    mov rsi, r13        ; from
    mov rdx, r14        ; to
    call printFromAndTo

    ; hanoi(n-1, aux, to, from)
    mov rdi, r12
    dec rdi             ; rdi = n-1
    mov rsi, r15        ; from = aux
    mov rdx, r14        ; to = original to
    mov rcx, r13        ; aux = original from
    call hanoi

    pop r15
    pop r14
    pop r13
    pop r12
    ret
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  End of your code  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

_start:
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; Start of your code ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Write code to take in number as input, then call hanoi(num, 'A','B','C')
    ; read input into buffer
    mov rax, 0
    mov rdi, 0
    mov rsi, input_buf
    mov rdx, 20
    syscall           

    ; Using the function given in the inlab task2
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

    ; calling hanoi(num, 'A','B','C')
    mov rdi, rax          ; n
    movzx rsi, byte [a_rod] ; from = 'A'
    movzx rdx, byte [b_rod] ; to   = 'B'
    movzx rcx, byte [c_rod] ; aux  = 'C'
    call hanoi
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;  End of your code  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi        ; status 0
    syscall