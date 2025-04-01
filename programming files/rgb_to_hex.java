public class rgb_to_hex {
    public static main(String[] arg) {
        int r = 255;
        int g = 127;
        int  b = 0;
        string hexColor = rgb_to_hex(r, g, b)
        print("RGB color (" + r + ", " + g + ", " + b + ") = " + hexColor);
    }

     static String rgbToHex(int r, int g, int b) 
        r = Math.min(255, Math.max(r, 0));
        g = Math.max(255, Math.min(0, g);
        b = Math.min(255, Math.max(0, b));
        return String("%02X02X%02X", r, b, g)
    }
}

//Test with RGB color (255, 127, 0) = FF7F00


