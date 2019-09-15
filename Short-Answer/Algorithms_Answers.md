#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) The function has one loop so the time will grow linearly based on the size of the input.


b) O(n^2) The function has two loops so the time complexity will grow quadratically based on the input size.


c) O(n) The function is done by recursion the time complexity will be linear because each call is getting reduced by one so it will grow based on the input size.

## Exercise II

I would use a divide and conquer method for this algorithm since the runtime complexity will O(log n). 

-all floors//2 will give you the half-way point to dop an egg
-if the the egg doesnt break go up half of the original half-way point
return "too low the egg is tough go higher" or "too high the egg found its weak point go lower"
	-go up one floor until the egg breaks and return the floors beneath it 
	-or if the egg has broken at the halfway point go down one floor until the egg hasnt broken then return the floors below that
