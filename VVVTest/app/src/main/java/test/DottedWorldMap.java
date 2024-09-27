package test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import test.App.Punkt;

public class DottedWorldMap {

    private static final String filePath = "src/main/resources/dotted_worldMap.txt";
    private static final String filePath2 = "src/main/resources/scaled_dotted_worldMap.txt";


    public static void readMap() {
        try (BufferedReader br = new BufferedReader(new FileReader(filePath2))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] coords = line.split(",");
                int x = Integer.parseInt(coords[0]);
                int y = Integer.parseInt(coords[1]);
                App.points.add(new Punkt(x, y));
            }
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println("Error reading file: " + filePath);
        }
    }
}