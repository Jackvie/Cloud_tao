class World {
	int age = 1;
	String name = "xiao";
	public void pri () {
		System.out.println(""+name+" " + age);
	}
}

public class Hello {
	public static void main(String args[]) {
		System.out.println("hello world!");
		System.out.print("hello world!");
		System.out.println("hello world!");
		// SET CLASSPATH=/home/wyt/Desktop/Cloud_tao/myjava
		// SET CLASSPATH=.
		/* 数据溢出 */
		int max = Integer.MAX_VALUE;
		int min= Integer.MIN_VALUE;
		System.out.println(max);
		System.out.println(min);
		// System.out.println(long(max)+1);
		World w = new World();
		w.age = 123;
		w.pri();
	}
}

