import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Programa {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] palabras = {
            "uno",
            "dos",
            "tres",
            "cuatro",
            "cinco",
            "seis",
            "siete",
            "ocho",
            "nueve",
            "diez"
        };

        Random random = new Random();
        String clave = palabras[random.nextInt(palabras.length)];

        List<Character> letrasRegistradas = new ArrayList<>();
        List<Character> letrasCorrectas = new ArrayList<>();

        int intentos = 5;
        boolean gana = false;

        while (intentos > 0 && !gana) {
            System.out.println("\n\t ..::  INTENTOS RESTANTES: " + intentos + "  ::..");

            char letra = pedirUnCaracter(
                scanner,
                "Introduce un solo caracter: ",
                letrasRegistradas
            );

            letrasRegistradas.add(letra);

            if (clave.indexOf(letra) != -1) {
                letrasCorrectas.add(letra);
                System.out.println(" LA LETRA " + letra + " SI ESTA EN LA PALABRA CLAVE ✅ ");

                gana = true;

                for (int i = 0; i < clave.length(); i++) {
                    char letraClave = clave.charAt(i);

                    if (!letrasCorrectas.contains(letraClave)) {
                        gana = false;
                        break;
                    }
                }
            } else {
                intentos--;
                System.out.println(" LA LETRA " + letra + " NO ESTA EN LA PALABRA CLAVE ❌ ");
            }

            String palabraMostrada = "";

            for (int i = 0; i < clave.length(); i++) {
                char letraClave = clave.charAt(i);

                if (letrasCorrectas.contains(letraClave)) {
                    palabraMostrada += letraClave;
                } else {
                    palabraMostrada += "_";
                }
            }

            System.out.println("Palabra: " + palabraMostrada);
        }

        System.out.println("=".repeat(50));

        if (gana) {
            System.out.println("\n\t FELICIDADES: LA PALABRA ES -> " + clave);
        } else {
            System.out.println("\n\t LA PALABRA ES -> " + clave);
        }

        System.out.println("\n\t ..::   PROGRAMA FINALIZADO   ::..");

        scanner.close();
    }

    public static char pedirUnCaracter(
        Scanner scanner,
        String mensaje,
        List<Character> letrasRegistradas
    ) {
        while (true) {
            System.out.print(mensaje);
            String entrada = scanner.nextLine().toLowerCase();

            if (entrada.length() != 1) {
                System.out.println("Error: Por favor, ingresa solo un caracter.");
            } else {
                char letra = entrada.charAt(0);

                if (letrasRegistradas.contains(letra)) {
                    System.out.println("Error: Por favor, ingresa una letra no repetida.");
                } else {
                    return letra;
                }
            }
        }
    }
}
