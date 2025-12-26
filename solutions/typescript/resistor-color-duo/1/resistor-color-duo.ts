const ColorMap: Record<string, number> = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
};


export function decodedValue(colors: string[]): number {
  // 1. Take the first two elements of the array
  // 2. Map the names to their numeric values
  // 3. Join them into a string and convert back to a number
  
  const [first, second] = colors;
  
  const val1 = ColorMap[first.toLowerCase()];
  const val2 = ColorMap[second.toLowerCase()];

  // Combine the digits (e.g., 1 and 5 becomes 15)
  return val1 * 10 + val2;
}
