import java.util.Base64;

public class Base64Decoder {
    public static void main(String[] args) {
        String encodedData = "AFIADgAAAXY3HR9H80AdMXvtc3EABgwHEQA/Pz8/P0J2IWdyJUlwIWYvRzBvcDhwSEhQNTFfek" +
                            "lfa0c/Pz8/Pz8AAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAkoRsQReobCuzXWhg9R8BAAEAAAAAAAAAAAAAAAAAAAAAAAA=";

        byte[] decodedBytes = Base64.getDecoder().decode(encodedData);
        String decodedString = new String(decodedBytes);

        // In ra kí tự thứ 3 và 4 của decodedString
        if (decodedString.length() >= 4) {
            char char3 = decodedString.charAt(2);
            char char4 = decodedString.charAt(3);
            System.out.println("Ki tu 3: " + char3);
            System.out.println("Ki tu 4: " + char4);
        } else {
            System.out.println("RIP");
        }
    }
}
