type OldFormat = { [key: string]: string[] };
type NewFormat = { [key: string]: number };

export function transform(old: OldFormat): NewFormat {
  const newSystem: NewFormat = {};

  for (const [score, letters] of Object.entries(old)) {
    const pointValue = Number(score);

    letters.forEach((letter) => {
      newSystem[letter.toLowerCase()] = pointValue;
    });
  }

  return newSystem;
}