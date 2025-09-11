section .data

complex1:
    complex1_name db 'a'
    complex1_pad  db 7 dup(0)  
    complex1_real dq 1.0
    complex1_img  dq 2.5

complex2:
    complex2_name db 'b'
    complex2_pad  db 7 dup(0)  
    complex2_real dq 3.5
    complex2_img  dq 4.0

polar_complx:
    polar_complx_name db 'c'
    polar_complx_pad db 7 dup(0)
    polar_complx_mag dq 10.0
    polar_complx_ang dq 0.0001

fmt db "%s => %f %f", 10, 0     ;
label_polar2rect db "Testing polars to rectangular",0
label_exp db "Testing exp",0
label_sin db "Testing sin",0
label_cos db "Testing cos",0

;;;;;;;;;;;;;
six dq 6.0
two dq 2.0
one dq 1.0
temp dq 0.0
;;;; Fill other constants needed 
fact4 dq 24.0   ; 4!
fact5 dq 120.0  ; 5!
fact6 dq 720.0  ; 6!
fact7 dq 5040.0 ; 7!
;;;;;;;;;;;;;

temp_cmplx:
    temp_name db 'r'
    temp_pad  db 7 dup(0)
    temp_real dq 0.0
    temp_img  dq 0.0

section .text
    default rel
    extern print_cmplx,print_float
    global main

main:
    push rbp
    
    ; --- Test: Polar to Rectangular ---
    lea rdi, [polar_complx]         ; pointer to input polar struct
    lea rsi, [temp_cmplx]     ; pointer to output rect struct
    
    call polars_to_rect

    lea rdi, [label_polar2rect]
    lea rsi, [temp_cmplx]
    call print_cmplx          ; should show converted rectangular form

    ; --- Test: exp ---
    movsd xmm0, [two]
    mov rdi, 0x6

    call exp

    movsd [temp],xmm0 
    lea rdi, [label_exp]
    lea rsi , [temp]
    call print_float

    ; --- Test: sin ---
    movsd xmm0, [two]

    call sin

    movsd [temp],xmm0 
    lea rdi, [label_sin]
    lea rsi , [temp]
    call print_float

    ; --- Test: cos ---
    movsd xmm0, [two]
    call cos

    movsd [temp],xmm0 
    lea rdi, [label_cos]
    lea rsi , [temp]
    call print_float

    mov     rax, 60         ; syscall: exit
    xor     rdi, rdi        ; status 0
    syscall


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; FILL FUNCTIONS BELOW ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; -----------------------------------
polars_to_rect:
    ; rdi -> polar struct address, rsi -> ret struct address
    push rbp
    
    mov rbp, rsp
    sub rsp, 32  ; allocating space in the stack to store r and theta

    movsd xmm0, [rdi + 8]
    movsd xmm1, [rdi + 16]

    ; saving r and theta on stack
    movsd [rsp], xmm0
    movsd [rsp + 8], xmm1 

    ; Calculating and storing real part of the rect struct
    movsd xmm0, [rsp + 8]
    call cos
    movsd xmm1, [rsp]
    mulsd xmm0, xmm1
    movsd [rsi + 8], xmm0

    ; Calculating and storing imaginary part of the rect struct
    movsd xmm0, [rsp + 8]
    call sin
    movsd xmm1, [rsp]
    mulsd xmm0, xmm1
    movsd [rsi + 16], xmm0

    ; deallocating the stack space
    add rsp, 32
    pop rbp
ret

;-------------------------------------------------
exp:
    ; Input xmm0 -> base, rdi -> power
    movsd xmm1, [one]
    cmp rdi, 0
    je exp_end
exp_loop:
    mulsd xmm1, xmm0
    dec rdi
    cmp rdi, 0
    jne exp_loop

exp_end:
    movsd xmm0, xmm1
    ret

;-------------------------------------------------
sin:
    ; Calculating sin(x) using Taylor Series (till 7th power of x)
    ; Input: xmm0 -> x
    push rbp

    mov rbp, rsp
    sub rsp, 32
    movsd [rbp - 8], xmm0

    ; calculating x^3/3!
    movsd xmm0, [rbp - 8]
    mov rdi, 3
    call exp
    divsd xmm0, [six]
    movsd [rbp - 16], xmm0

    ; calculating x^5/5!
    movsd xmm0, [rbp - 8]
    mov rdi, 5
    call exp
    divsd xmm0, [fact5]
    movsd [rbp - 24], xmm0

    ; calculating x^7/7!
    movsd xmm0, [rbp - 8]
    mov rdi, 7
    call exp
    divsd xmm0, [fact7]
    movsd [rbp - 32], xmm0

    ; combining terms
    movsd xmm0, [rbp - 8]
    subsd xmm0, [rbp - 16]
    addsd xmm0, [rbp -24]
    subsd xmm0, [rbp - 32]

    ; deallocating stack
    mov rsp, rbp
    pop rbp
ret
cos:
    ; Calculating cos(x) using Taylor Series (till 7th power of x)
    ; Input: xmm0 -> x
    push rbp

    mov rbp, rsp
    sub rsp, 32
    movsd [rbp - 8], xmm0

    ; calculating x^2/2!
    movsd xmm0, [rbp - 8]
    mov rdi, 2
    call exp
    divsd xmm0, [two]
    movsd [rbp - 16], xmm0

    ; calculating x^4/4!
    movsd xmm0, [rbp - 8]
    mov rdi, 4
    call exp
    divsd xmm0, [fact4]
    movsd [rbp - 24], xmm0

    ; calculating x^6/6!
    movsd xmm0, [rbp - 8]
    mov rdi, 6
    call exp
    divsd xmm0, [fact6]
    movsd [rbp - 32], xmm0

    ; combining terms
    movsd xmm0, [one]
    subsd xmm0, [rbp - 16]
    addsd xmm0, [rbp - 24]
    subsd xmm0, [rbp - 32]

    ; deallocating stack
    mov rsp, rbp
    pop rbp
ret
;-------------------------------------------------
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; CODE ENDS HERE ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
