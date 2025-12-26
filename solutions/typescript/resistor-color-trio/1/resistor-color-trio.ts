const ColorMap = {
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
} as const;

type Color = keyof typeof ColorMap;

export function decodedResistorValue([band1, band2, band3]: Color[]): string {
  const mainValue = (ColorMap[band1] * 10) + ColorMap[band2];
  const totalOhms = mainValue * Math.pow(10, ColorMap[band3]);

  if (totalOhms >= 1_000_000_000) {
    return `${totalOhms / 1_000_000_000} gigaohms`;
  } else if (totalOhms >= 1_000_000) {
    return `${totalOhms / 1_000_000} megaohms`;
  } else if (totalOhms >= 1_000) {
    return `${totalOhms / 1_000} kiloohms`;
  }

  return `${totalOhms} ohms`;
}