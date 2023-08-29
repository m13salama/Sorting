public class SleepSort {
    public static void main(String[] args) {
        int[] arr = {54, 23, 1220, 9};
        sleepSort(arr);
    }
    public static void sleepSort(int[] arr) {
        Thread[] threads = new Thread[arr.length];

        for (int i = 0; i < arr.length; i++) {
            final int num = arr[i];
            threads[i] = new Thread(() -> {
                try {
                    Thread.sleep(10*num);
                    System.out.print(num + " ");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            });
            threads[i].start();
        }

        for (Thread thread : threads) {
            try {
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println();
    }
}
