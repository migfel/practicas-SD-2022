iMac-de-Miguel:Desktop LabMigfel$ gcc -o fibo fibonacci.c
iMac-de-Miguel:Desktop LabMigfel$ otool -tv fibo
fibo:
(__TEXT,__text) section
_main:
0000000100000f30	pushq	%rbp
0000000100000f31	movq	%rsp, %rbp
0000000100000f34	subq	$0x20, %rsp
0000000100000f38	movl	$0x0, -0x4(%rbp)
0000000100000f3f	movl	$0x0, -0x8(%rbp)
0000000100000f46	movl	$0x1, -0xc(%rbp)
0000000100000f4d	leaq	0x56(%rip), %rdi
0000000100000f54	movl	-0x8(%rbp), %esi
0000000100000f57	movb	$0x0, %al
0000000100000f59	callq	0x100000f88
0000000100000f5e	movl	-0x8(%rbp), %esi
0000000100000f61	addl	-0xc(%rbp), %esi
0000000100000f64	movl	%esi, -0x10(%rbp)
0000000100000f67	movl	-0xc(%rbp), %esi
0000000100000f6a	movl	%esi, -0x8(%rbp)
0000000100000f6d	movl	-0x10(%rbp), %esi
0000000100000f70	movl	%esi, -0xc(%rbp)
0000000100000f73	movl	%eax, -0x14(%rbp)
0000000100000f76	cmpl	$0xff, -0x8(%rbp)
0000000100000f7d	jl	0x100000f4d
0000000100000f83	jmp	0x100000f3f
iMac-de-Miguel:Desktop LabMigfel$ 
