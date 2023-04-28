import java.io.*;

public class FileFragmenter {
    public static void main(String[] args) throws IOException {
        String filename = "archivotransferir.txt";
        File file = new File(filename);
        long fileSize = file.length();
        long chunkSize = fileSize / 10;
        
        try (BufferedInputStream bis = new BufferedInputStream(new FileInputStream(file))) {
            byte[] buffer = new byte[(int) chunkSize];
            int bytesRead = 0;
            int index = 1;
            while ((bytesRead = bis.read(buffer)) != -1) {
                ByteArrayOutputStream baos = new ByteArrayOutputStream();
                baos.write(buffer, 0, bytesRead);
                byte[] chunk = baos.toByteArray();
                // Aquí se puede llamar un método remoto para transferir cada fragmento utilizando RMI Java.
                index++;
            }
        }
    }
}
