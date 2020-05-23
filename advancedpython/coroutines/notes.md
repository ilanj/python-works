<h2> coroutines </h2>

 - function which is also known as a subroutine, procedure, subprocess etc. 
 
- Subroutines in Python are called by main function which is responsible for coordination the
  use of these subroutines. Subroutines have single entry point.
  
 - Coroutines are generalization of subroutines. They are used for cooperative multitasking
   where a process voluntarily yield (give away) control periodically or when idle in order to enable multiple applications to be run simultaneously.
   
  - Unlike subroutines, coroutines have many entry points for suspending and resuming execution. 
   
  - Unlike subroutines, there is no main function to call coroutines in particular order 
   and coordinate the results. Coroutines are cooperative that means they link together 
   to form a pipeline. One coroutine may consume input data and send it to other which 
   process it. Finally there may be a coroutine to display result.