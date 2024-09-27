package test;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class App extends Application {
    // Liste für die Punkte
    public static List<Punkt> points = new ArrayList<>();
    private int clickCounter = 0; // Click counter
    private static final int CLICKED = 4;

    // Punkt-Klasse
    public static class Punkt {
        int row, col;
        boolean liegtAmWasser, hatFlughafen, hatBahnhof;
        int co2Belastung; // CO2-Wert
        Circle circle; // Repräsentation des Punktes als Kreis

        Punkt(int row, int col) {
            this(row, col, false, false, false, 30); // Set initial CO2 value to 30 (neutral)
        }

        Punkt(int row, int col, boolean liegtAmWasser, boolean hatFlughafen, boolean hatBahnhof, int co2Belastung) {
            this.row = row;
            this.col = col;
            this.liegtAmWasser = liegtAmWasser;
            this.hatFlughafen = hatFlughafen;
            this.hatBahnhof = hatBahnhof;
            this.co2Belastung = co2Belastung;
            this.circle = new Circle(5, getColor());
        }

        public int x() {
            return col;
        }

        public int y() {
            return row;
        }

        // Methode zum Bestimmen der Farbe basierend auf dem CO2-Wert
        public Color getColor() {
            if (co2Belastung >= 60) {
                return Color.RED; // Very high CO2 score
            } else if (co2Belastung >= 50) {
                return Color.DARKRED; // High CO2 score
            } else if (co2Belastung >= 40) {
                return Color.ORANGE; // Moderately high CO2 score
            } else if (co2Belastung >= 30) {
                return Color.GRAY; // Neutral
            } else if (co2Belastung >= 20) {
                return Color.LIME; // Moderately low CO2 score
            } else if (co2Belastung >= 10) {
                return Color.LIMEGREEN; // Low CO2 score
            } else {
                return Color.DARKGREEN; // Very low CO2 score
            }
        }
    }

    @Override
    public void start(Stage primaryStage) {
        // Read the map to populate the points list
        DottedWorldMap.readMap();
        GridPane grid = new GridPane();
        // Punkte zum GridPane hinzufügen
        for (Punkt point : points) {
            point.circle.setOnMouseClicked(event -> handlePointClick(point));
            grid.add(point.circle, point.col, point.row);
        }
        // Scene und Stage einrichten
        Scene scene = new Scene(grid, 800, 600);
        primaryStage.setTitle("Dotted World Map with Attributes");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // Methode zum Behandeln von Klicks auf Punkte
    private void handlePointClick(Punkt point) {
        clickCounter++;
        boolean isTimesClicked = clickCounter % CLICKED == 0;

        if (isTimesClicked) {
            // Get neighboring points and update their CO2 value
            point.co2Belastung = 60;
            point.circle.setFill(point.getColor()); // Update the color of the circle
            List<Punkt> neighbors = getNeighbors(point);
            for (Punkt neighbor : neighbors) {
                double distance = Math
                        .sqrt(Math.pow(neighbor.row - point.row, 2) + Math.pow(neighbor.col - point.col, 2));
                if (distance <= 2) {
                    neighbor.co2Belastung = 60; // Set CO2 value to 5 if it's higher than 5
                } else if (distance <= 5) {
                    if (neighbor.co2Belastung < 50) {
                        neighbor.co2Belastung = 50; // Set CO2 value to 10 if it's higher than 10
                    }
                } else if (distance <= 9) {
                    if (neighbor.co2Belastung < 40) {
                        neighbor.co2Belastung = 40; // Set CO2 value to 20 if it's higher than 20
                    }
                }
                neighbor.circle.setFill(neighbor.getColor()); // Update the color of the circle
            }
        } else {
            // Handle green points
            if (point.co2Belastung != 60)
                point.co2Belastung = 0; // Set a special value to indicate the point is clicked
                point.circle.setFill(point.getColor()); // Update the color of the circle to green

            // Get neighboring points and update their CO2 value
            List<Punkt> neighbors = getNeighbors(point);
            for (Punkt neighbor : neighbors) {
                double distance = Math
                        .sqrt(Math.pow(neighbor.row - point.row, 2) + Math.pow(neighbor.col - point.col, 2));
                if (distance <= 1) {
                    if (neighbor.co2Belastung != 60)
                        neighbor.co2Belastung = 0; // Set CO2 value to 5 if it's higher than 5
                } else if (distance <= 3) {
                    if (neighbor.co2Belastung > 10 && neighbor.co2Belastung != 60) {
                        neighbor.co2Belastung = 10; // Set CO2 value to 10 if it's higher than 10
                    }
                } else if (distance <= 5) {
                    if (neighbor.co2Belastung > 20 && neighbor.co2Belastung != 60) {
                        neighbor.co2Belastung = 20; // Set CO2 value to 20 if it's higher than 20
                    }
                }
                neighbor.circle.setFill(neighbor.getColor()); // Update the color of the circle
            }
        }
    }

    // Methode zum Ermitteln der Nachbarpunkte im Radius von 4
    private List<Punkt> getNeighbors(Punkt point) {
        List<Punkt> neighbors = new ArrayList<>();
        for (Punkt p : points) {
            double distance = Math.sqrt(Math.pow(p.row - point.row, 2) + Math.pow(p.col - point.col, 2));
            if (distance <= 20 && p != point) {
                neighbors.add(p);
            }
        }
        return neighbors;
    }

    public static void main(String[] args) {
        launch(args);
    }
}