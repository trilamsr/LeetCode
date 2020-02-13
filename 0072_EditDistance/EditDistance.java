import java.lang.Math;

public class Quoori {

    private static int levenshtein(String token1, String token2, int maxDist) {
        int m = 1 + token1.length();
        int n = 1 + token2.length();
        int[] dp = new int[n];

        boolean exitEarly = false;
        
        for (int i = 0; i < m && !exitEarly; i++) {
            int[] curDP = new int[n];
            int curDist = Integer.MAX_VALUE;
            for (int j = 0; j < n && !exitEarly; j++) {
                if (i== 0 || j ==0) {
                    curDP[j] = i == 0 ? j : i;
                } else if (token1.charAt(i-1) == token2.charAt(j-1)) {
                    curDP[j] = dp[j-1];
                } else {
                    int opt1 = dp[j];
                    int opt2 = dp[j-1];
                    int opt3 = curDP[j-1];
                    int minCost = Math.min(opt1, Math.min(opt2, opt3));
                    curDP[j] = 1 + minCost;
                }
                curDist = Math.min(curDP[j], curDist);
            }
            exitEarly = curDist > maxDist;
            dp = curDP;
        }
        int result = exitEarly ? maxDist + 1 : dp[n-1];
        return result;
    }

    private static int levenshtein(String token1, String token2) {
        int m = 1 + token1.length(), n = 1 + token2.length();
        int[] dp = new int[n]; 
        for (int i = 0; i < m; i++) {
            int[] curDP = new int[n];
            for (int j = 0; j < n; j++) {
                if (i== 0 || j ==0)
                    curDP[j] = i == 0 ? j : i;
                else if (token1.charAt(i-1) == token2.charAt(j-1))
                    curDP[j] = dp[j-1];
                else {
                    int opt1 = dp[j];
                    int opt2 = dp[j-1];
                    int opt3 = curDP[j-1];
                    curDP[j] = 1 + Math.min(opt1, Math.min(opt2, opt3));
                }
            }
            dp = curDP;
        }
        return dp[n-1];
    }

    public static void main(String[] args) {
        Tests.benchmarkLevenshteinDistance(Tests.Version.ORIGINAL);
        Tests.benchmarkLevenshteinDistance(Tests.Version.MODIFIED);
    }

    private static class Tests {

        protected enum Version {
            ORIGINAL, 
            MODIFIED;
        }

        private static String[][] tests = {
            {"Haus", "Maus", "2"},
            {"Haus", "Mausi", "2"},
            {"Haus", "Häuser", "2"},
            {"Kartoffelsalat", "Runkelrüben", "2"},
        };

        private static int[][] expected = {
            {1,1},
            {2,2},
            {3,3},
            {12,3}
        };


        private static void benchmarkLevenshteinDistance(Version version) {
            boolean isOriginal = version.equals(Version.ORIGINAL);
            String strVersion = isOriginal ? "Original"  : "Modified";
            int expectedVersion = isOriginal ? 0 : 1;
            long totalElapsedTime = 0;

            for (int testCase = 0; testCase < tests.length; testCase++) {
                String[] inputs = tests[testCase];
                String token1 = inputs[0];
                String token2 = inputs[1];
                int maxDistance = isOriginal 
                    ? Integer.MAX_VALUE 
                    : Integer.parseInt(inputs[2]);

                long start = System.nanoTime();
                int result = Quoori.levenshtein(token1, token2, maxDistance);
                long elapsed = System.nanoTime() - start;
                totalElapsedTime += elapsed;

                String template = "   Case %s: %s and %s. Output: %d. Expected: %d";
                String output = String.format(
                    template, 
                    strVersion,
                    token1, 
                    token2, 
                    result, 
                    expected[testCase][expectedVersion]
                );
                System.out.println(output);
            }
            double totalMilliseconds = (double) totalElapsedTime / 1000000;
            System.out.println("Total execution time in milliseconds: " + totalMilliseconds);
        }

    }
}