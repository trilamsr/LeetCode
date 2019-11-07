public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        // So Java has the feature you want, but with a few extra steps. You need to define an interface to wrap the call in
        // addition
        doMyThing(a,b, new MyCaller() {
            public void callback(int a, int b) {System.out.println(a+b);}
        });
        // multiplication.
        // here I utilize the doMyThing function, and I implement an anonymous instance of my interface: new MyCaller()...
        // Then I just Override the function callback, to decide what my code should do in this instance.
        // Instead of doing it in-line, you could also do a non anonymous implementation.
        doMyThing(a,b, new MyCaller() {
            @Override
            public void callback(int a, int b) {
                System.out.println(a*b);
            }
        });
        // with named "callback"
        doMyThing(a,b, new Adder());
    }
  // Now here, I define a function that "consumes" my interface. It knows that MyCaller has a method named callback, and that callback takes two int arguments.
    public static void doMyThing(int a, int b, MyCaller function) {
        function.callback(a,b);
    }
  // This interface is my callback function, which is passed along. In JS, it would just be a function.
  // Java is a bit more uh.. special needs. It wants types for everything.
    interface MyCaller {
        void callback(int a, int b);
    }
  // Here we implement a named implementation as my callback, and I could add that as my parameter.
    static class Adder implements MyCaller {
        public void callback(int a, int b) {
        System.out.println(a+b);
        }
    }
}







