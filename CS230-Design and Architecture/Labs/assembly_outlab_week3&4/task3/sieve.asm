section .data
    buffer db 20 dup(0)
    buff_len equ $ - buffer

section .text
    global _start

; NOTE: IN THE FOLLOWING COMMENTS, '*' COULD 
; MEAN EITHER A MEMORY DEREFERENCE OR A MULTIPLICATION
; IT SHOULD BE CLEAR WITH CONTEXT

_start:

    ; read(0, buffer, buff_len)
    mov rax,0
    mov rdi,0
    mov rsi,buffer
    mov rdx,buff_len
    syscall

    ; now convert number to integer
    mov rsi, buffer  ; rsi points to buffer
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
    ; the input number is stored inside rax
    
;;;;;;;;;;;;;;;;; Task 1 : allocate memory ;;;;;;;;;;;;;;;;;;;;;
; Allocate memory for arr
; How to get arr?
; Two uses of the brk syscall (syscall number = 12)
; arr = brk(0);
; brk(arr + n*8); Why 8? Each element of arr is of 8 bytes.

    mov rbx, rax  ; temporarily saving n in rbx
    mov rax, 12
    xor rdi, rdi
    syscall
    mov rdi, rax

    mov rax, rbx
    shl rax, 3   ; multiplying n by 8
    add rdi, rax

    mov rax, 12
    syscall
;;;;;;;;;;;;;;;;;; Task 2 : Store local variables ;;;;;;;;;;;;;;;;;;;
; Store local variables (n and arr) in the stack
; Subtract 16 from the stack pointer to make space for them
; That is, rsp -= 16
; Now, *(rsp) = n
; *(rsp + 8) = arr

    mov rax, rbx
    shl rax, 3
    sub rdi, rax
    sub rsp, 16
    mov [rsp], rbx
    mov [rsp + 8], rdi

;;;;;;;;;;;;;;;;;;; Task 3 : For loop 1 ;;;;;;;;;;;;;;;
; Make space on the stack for i
; That is, rsp -= 8
; Note now, *(rsp) = i, *(rsp + 8) = n and *(rsp + 16) = arr
; Store 0 in i, that is *(rsp) = 0
    sub rsp, 8
    mov qword [rsp], 0
.for1Begin:
    ; Write code to jump to for1End if i >= n
    mov rcx, [rsp]
    mov rdx, [rsp + 8]
    cmp rcx, rdx
    jge .for1End
    ; Do array[i] = 0
    ; *(*(rsp + 16) + i*8) = 0 (Why 8? Because each element of the array is of 8 bytes)
    mov rbx, [rsp + 16]
    mov qword [rbx + rcx*8], 0
    ; load and increment i
    ; That is, *(rsp)++;
    ; Jump to for1Begin
    inc qword [rsp]
    jmp .for1Begin
.for1End:
; Restore stack, rsp += 8
    add rsp, 8
;;;;;;;;;;;;;;;;;; Task 4 : For loop 2 ;;;;;;;;;;;;;;;;;;;;;
; Make space on the stack for i
; That is, rsp -= 8
; Note now, *(rsp) = i, *(rsp + 8) = n and *(rsp + 16) = arr
; Store 2 in i, that is *(rsp) = 2
    sub rsp, 8
    mov qword [rsp], 2
.for2Begin:
    ; Write code to jump to for2End if i >= n
    mov rcx, [rsp]
    mov rdx, [rsp + 8]
    cmp rcx, rdx
    jge .for2End
    ; Write code to jump to else if array[i] != 0
    ; *(*(rsp + 16) + i*8) = array[i]
    mov rbx, [rsp + 16]
    mov rax, [rbx + rcx*8]
    cmp rax, 0
    jne .else
.if:
    ; Make space on the stack for j
    ; That is, rsp -= 8
    ; Note now, *(rsp) = j. *(rsp + 8) = i, *(rsp + 16) = n and *(rsp + 24) = arr
    ; Store i * 2 in j, that is *(rsp) = 2 * *(rsp + 8)
    sub rsp, 8
    mov rax, [rsp + 8]
    shl rax, 1
    mov [rsp], rax
    .innerForBegin:
        ; Write code to jump to innerForEnd if j >= i
        mov rax, [rsp]
        mov rdx, [rsp + 16]
        cmp rax, rdx
        jge .innerForEnd
        ; Write code to jump to innerElse if array[j] != 0
        ; *(*(rsp + 24) + j * 8) = array[j]
        mov rbx, [rsp + 24]
        mov r10, [rbx + rax*8]
        cmp r10, 0
        jne .innerElse
        .innerIf:
        ; array[j] = i
        ; That is, *(*(rsp + 24) + j*8) = *(rsp + 8)
        mov r11, [rsp + 8]
        mov [rbx + rax*8], r11
        .innerElse:
        ; Load and do j += i
        ; That is, *(rsp) += *(rsp + 8)
        ; Jump to innerForBegin
        mov r11, [rsp + 8]
        add [rsp], r11
        jmp .innerForBegin
    .innerForEnd:
    ; Restore the stack, rsp += 8
    add rsp, 8
.else:
    ; load and increment i
    ; That is, *(rsp)++;
    ; Jump to for2Begin
    inc qword [rsp]
    jmp .for2Begin
.for2End:
; Restore stack, rsp += 8
    add rsp, 8
;;;;;;;;;;;;;;;;;;; Task 5 : For loop 3 ;;;;;;;;;;;;;;;;;;;;;
; Make space on the stack for i
; That is, rsp -= 8
; Note now, *(rsp) = i, *(rsp + 8) = n and *(rsp + 16) = arr
; Store 0 in i, that is *(rsp) = 0
    sub rsp, 8
    mov qword [rsp], 2
.for3Begin:
; Write code to jump to for3End if i >= n
    mov rcx, [rsp]
    mov rdx, [rsp + 8]
    cmp rcx, rdx
    jge .for3End
; rax = array[i]
; That is, rax = *(*(rsp + 16) + i*8)
    mov rbx, [rsp + 16]
    mov rax, [rbx + rcx*8]
    
.convert_loop_start:
    ; Prints the number stored in rax to stdout
    mov rdi, buffer + 19 ; Start from the end of the buffer
    mov rbx, 10          ; Base 10 for conversion
    mov rcx, 0           ; Digit count
.convert_loop:
    xor rdx, rdx         ; Clear rdx for division
    div rbx              ; rax = rax / 10, rdx = rax % 10
    add rdx, '0'         ; Convert digit to ASCII
    mov [rdi], dl        ; Store the digit in the buffer
    dec rdi              ; Move buffer pointer backwards    
    inc rcx              ; Increment digit count
    test rax, rax        ; Check if rax is zero
    jnz .convert_loop     ; If not zero, continue converting
    
    inc rdi
    mov rax, 1          ; syscall: write
    mov rsi, rdi        ; rsi points to the start of the string
    mov rdi, 1          ; file descriptor: stdout
    mov rdx, rcx        ; rdx is the number of digits
    syscall             ; Write the string to stdout


; load and increment i
; That is, *(rsp)++;
; Jump to for2Begin
    inc qword [rsp]
    jmp .for3Begin
.for3End:
; Restore stack, rsp += 8
    add rsp, 8
    mov rax, 60
    xor rdi, rdi
    syscall