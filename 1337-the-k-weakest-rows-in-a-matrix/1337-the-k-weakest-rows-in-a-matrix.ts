function kWeakestRows(mat: number[][], k: number): number[] {
    
      const result = [];

      let rowIndex = 0;
      for (const row of mat) {
        let counterSoldier = row.reduce(
          (accomulator, currentValue) => accomulator + currentValue,
          0
        );
        const soldier = [counterSoldier, rowIndex];
        result.push(soldier);
        rowIndex++;
      }

      result.sort((a, b) => a[0] - b[0]);

      return result.slice(0, k).map((rowIndex) => rowIndex[1]);
    
};