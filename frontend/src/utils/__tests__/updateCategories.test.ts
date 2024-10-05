import { Category } from '../../types';
import { updateCategories } from '../updateCategories';

describe('test apply categories function', () => {
    const testCases = [
        {
            selectedCategories: ["Для дома", "Одежда", "Электроника"],
            clickedCategory: "Для дома",
            expected: ["Одежда", "Электроника"],
        },
        {
            selectedCategories: ["Одежда", "Электроника"],
            clickedCategory: "Одежда",
            expected: ["Электроника"],
        },
        {
            selectedCategories: ["Электроника"],
            clickedCategory: "Электроника",
            expected: [],
        },
        {
            selectedCategories: ["Для дома", "Электроника"],
            clickedCategory: "Одежда",
            expected: ["Для дома", "Электроника", "Одежда"],
        },
    ];

    testCases.forEach(({ selectedCategories, clickedCategory, expected }) => {
        it(`should return ${JSON.stringify(expected)} when clicked category is "${clickedCategory}"`, () => {
            expect(updateCategories(selectedCategories as Category[], clickedCategory as Category)).toStrictEqual(expected);
        });
    });
});
