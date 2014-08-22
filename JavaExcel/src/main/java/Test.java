/**
 * Created by chenliang on 14-7-4.
 */
public class Test {
  static int a = 3;



  public static void main(String[] args) {


    MyInterface myInterface = new MyInterface() {
      @Override
      public void fun() {
        System.out.println(a);
      }
    };
    myInterface.fun();


    a ++;



  }
}

interface MyInterface {
  public void fun();
}