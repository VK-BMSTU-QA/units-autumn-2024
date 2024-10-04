import { updateCategories } from "../updateCategories";

describe('test update categories function', () => {
    it('should include or exclude chosen category from categories list', () => {
        expect(updateCategories(['Для дома','Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда', 'Электроника']);
        expect(updateCategories(['Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда','Электроника','Для дома']);
    })
});