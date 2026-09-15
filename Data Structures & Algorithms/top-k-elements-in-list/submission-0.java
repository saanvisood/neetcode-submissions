class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.merge(num, 1, Integer::sum);
        }
        int[] kElements = new int[k];
        for (int i = 0; i < k; i++) {
            int maxKey = countMap.entrySet().stream()
                        .max(Map.Entry.comparingByValue())
                        .map(Map.Entry::getKey)
                        .orElse(null);
            kElements[i] = maxKey;
            countMap.remove(maxKey);
        }
        return kElements;
    }
}