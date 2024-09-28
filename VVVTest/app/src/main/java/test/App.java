package test;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.Image;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.stage.Stage;

import java.util.ArrayList;
import java.util.List;

public class App extends Application {
    public static List<Punkt> points = new ArrayList<>();
    private int clickCounter = 0;
    private static final int CLICKED = 4;

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
        DottedWorldMap.readMap();
        GridPane grid = new GridPane();
        grid.setPadding(new Insets(70, 0, 0, 35));

        for (Punkt point : points) {
            point.circle.setOnMouseClicked(event -> handlePointClick(point));
            grid.add(point.circle, point.col, point.row);
        }

        ScrollPane scrollPane = new ScrollPane(grid);



        Scene scene = new Scene(scrollPane, 1400, 800);
        primaryStage.setTitle("Dotted World Map with Attributes");
        Image icon = new Image("Logo-VVV.png");
        primaryStage.getIcons().add(icon);
        primaryStage.setScene(scene);
        primaryStage.setMaximized(true);
        primaryStage.show();
    }

    private void handlePointClick(Punkt point) {
        clickCounter++;
        boolean isTimesClicked = clickCounter % CLICKED == 0;

        if (isTimesClicked) {
            point.co2Belastung = 60;
            point.circle.setFill(point.getColor());
            List<Punkt> neighbors = getNeighbors(point);
            for (Punkt neighbor : neighbors) {
                double distance = Math
                        .sqrt(Math.pow(neighbor.row - point.row, 2) + Math.pow(neighbor.col - point.col, 2));
                if (distance <= 2) {
                    neighbor.co2Belastung = 60;
                } else if (distance <= 5) {
                    if (neighbor.co2Belastung < 50) {
                        neighbor.co2Belastung = 50;
                    }
                } else if (distance <= 9) {
                    if (neighbor.co2Belastung < 40) {
                        neighbor.co2Belastung = 40;
                    }
                }
                neighbor.circle.setFill(neighbor.getColor());
            }
        } else {
            if (point.co2Belastung != 60) // cant change fully red points
                point.co2Belastung = 0;
            point.circle.setFill(point.getColor());

            List<Punkt> neighbors = getNeighbors(point);
            for (Punkt neighbor : neighbors) {
                double distance = Math
                        .sqrt(Math.pow(neighbor.row - point.row, 2) + Math.pow(neighbor.col - point.col, 2));
                if (distance <= 1) {
                    if (neighbor.co2Belastung != 60) // cant change fully red points
                        neighbor.co2Belastung = 0;
                } else if (distance <= 3) {
                    if (neighbor.co2Belastung > 10 && neighbor.co2Belastung != 60) {
                        neighbor.co2Belastung = 10;
                    }
                } else if (distance <= 5) {
                    if (neighbor.co2Belastung > 20 && neighbor.co2Belastung != 60) {
                        neighbor.co2Belastung = 20;
                    }
                }
                neighbor.circle.setFill(neighbor.getColor());
            }
        }
    }

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