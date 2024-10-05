import { updateCategories } from "../updateCategories";

describe('test to update the category', () => {
    it('enables or disables a category from the list', () => {
        expect(updateCategories(['Для дома'], 'Для дома')).toStrictEqual([]);
        expect(updateCategories([], 'Для дома')).toStrictEqual(['Для дома']);
        expect(updateCategories(['Одежда'], 'Для дома')).toStrictEqual(['Одежда','Для дома']);
        expect(updateCategories(['Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда','Электроника','Для дома']);
        expect(updateCategories(['Для дома','Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда', 'Электроника']);
    })
});