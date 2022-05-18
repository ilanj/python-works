THREADS ARE SUBSET OF A PROCESS -Processes do not share the same memory space, while threads do 

True parallelism can ONLY be achieved using multiprocessing

Multithreading for I/O intensive tasks and;
Multiprocessing for CPU intensive tasks (if you have multiple cores available)

Processes execution is scheduled by the operating system, while threads are scheduled by the GIL.

Thread: (sharing)  is the unit of execution within a process. A process can have multiple threads running as a part of it, 
where each thread uses the process’s memory space and shares it with other threads.

Process: (independent) part of a program which is loaded into memory for execution, and it has its own memory space.

Multithreading: is a technique where multiple threads are spawned by a process to do different tasks, at about the same 
time, just one after the other. This gives you the illusion that the threads are running in parallel, but they are actually 
run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.

Multiprocessing: is a technique where parallelism in its truest form is achieved. Multiple processes are run across multiple 
CPU cores, which do not share the resources among them. Each process can have many threads running in its own memory space. 
In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.

reference: https://towardsdatascience.com/multithreading-vs-multiprocessing-in-python-3afeb73e105f

