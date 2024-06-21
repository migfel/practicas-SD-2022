import java.io.*;
import java.security.*;
import java.math.BigInteger;
import org.json.JSONObject;
import org.json.JSONArray;

public class Torrent{
	
	static final int PEDAZO_TAM = 102400; //bytes
	static final int MAX_PETICION = 10;

    static final String HASH_ALGORITHM = "MD5";

    String id;
	String tracker;
    int puertoTracker;
	int pedazos;
	int ultimo_pedazo;
	String nombre;
	String archivo;
	Boolean[] obtenidos;
    String[] checksum;
	
	// Parsear el .torrent 
	Torrent(String torrentPath) throws IOException{
		File file = new File(torrentPath);
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		String line = br.readLine();
		if( line != null ) {
			JSONObject obj = new JSONObject(line);
            id = obj.getString("id");
			tracker = obj.getString("tracker");
            puertoTracker = obj.getInt("puertoTracker");
			pedazos = obj.getInt("pieces");
			ultimo_pedazo = obj.getInt("lastPiece");
			nombre = obj.getString("name");	
			archivo = obj.getString("filepath");
            // Checksum
            JSONArray checksumJSON = obj.getJSONArray("checksum");
            checksum = new String[checksumJSON.length()];
            for(int i = 0, l = checksumJSON.length(); i < l; i++) {
                checksum[i] = checksumJSON.getString(i);
            }
		}
		br.close();
		fr.close();
		obtenidos = new Boolean[pedazos];
	}

    public Boolean isPieceValid(byte[] piece, int index) {
        try { 
            MessageDigest m = MessageDigest.getInstance(HASH_ALGORITHM);
            return hash(m, piece).equals( checksum[index] );
        }
        catch(NoSuchAlgorithmException e) {
            e.printStackTrace();
            return false;
        }
    }

	public static void main(String args[]) throws NoSuchAlgorithmException {
		// Crear torrent
        if( args.length == 3) {
            try{ 
                // Variable general para el hash
                MessageDigest m = MessageDigest.getInstance(HASH_ALGORITHM);
                // Abrir archivo
                String file_path = "archivos/"+args[2];
                File fileObj = new File(file_path);
                if( fileObj.exists() ){
                    // Sacar el nombre del archivo
                    String fileName = fileObj.getName();
                    int pos = fileName.lastIndexOf(".");
                    if (pos > 0) {
                        fileName = fileName.substring(0, pos);
                    }
                    // Calcular la cantidad de pedazos y el tamaño del ultimo pedazo
                    double fileSize = fileObj.length();
                    int piecesQty = (int)Math.ceil( fileSize/Torrent.PEDAZO_TAM );
                    int lastPiece = 0;
                    if( piecesQty*Torrent.PEDAZO_TAM > fileSize)
                        lastPiece = (int)(fileSize - ( piecesQty-1)*Torrent.PEDAZO_TAM);
                    // Sacar el checksum de cada pedazo
                    JSONArray checksum = new JSONArray();
                    InputStream is = new FileInputStream(file_path);
                    for(int i = 0; i < piecesQty; i++) {
                        byte[] data = new byte[Torrent.PEDAZO_TAM];
                        if( i < piecesQty-1) {
                            is.read(data, 0, Torrent.PEDAZO_TAM);
                        }
                        else if( i == piecesQty - 1 ){
                            data = new byte[lastPiece];
                            is.read(data, 0, lastPiece);
                        }
                        // Hash
                        checksum.put(hash(m, data) );
                    }
                    is.close();
                    // Obtener la direccion del tracker
                    String ip = args[0];
                    int puertoTracker = Integer.parseInt(args[1]);
                    // Crear el archivo de salida
                    FileOutputStream fos = new FileOutputStream("torrents/"+fileName+".torrent");
                    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(fos));
                    // Crear el torrent de este archivo como un JSON
                    JSONObject torrentObj = new JSONObject();
                    torrentObj.put("tracker", ip);
                    torrentObj.put("pieces", piecesQty);
                    torrentObj.put("lastPiece", lastPiece);
                    torrentObj.put("filepath", file_path);
                    torrentObj.put("name", fileObj.getName());
                    torrentObj.put("puertoTracker", puertoTracker);
                    torrentObj.put("checksum", checksum);
                    // Generar ID unico
                    torrentObj.put("id", hash(m, fileName.getBytes()) );
                    // Guardar en el archivo
                    bw.write( torrentObj.toString() );
                    bw.close();
                    fos.close();
                    System.out.println("Torrent creado!");
                    return;
                }
            }
            catch(FileNotFoundException fe) {fe.printStackTrace();}
            catch(IOException ie) {ie.printStackTrace();}
        }
        // Mostrar error
        System.out.println("Usage: ");
        System.out.println("java Torrent <tracker_ip> <puerto_tracker> <file_name en archivos>");   
	}

    public static String hash(MessageDigest messageDigest, byte[] data) throws NoSuchAlgorithmException {
        messageDigest.reset();
        messageDigest.update(data);
        byte[] digest = messageDigest.digest();
        BigInteger bigInt = new BigInteger(1,digest);
        String hashtext = bigInt.toString(16);
        while(hashtext.length() < 32 ){
            hashtext = "0"+hashtext;
        }
        return hashtext;
    }

}