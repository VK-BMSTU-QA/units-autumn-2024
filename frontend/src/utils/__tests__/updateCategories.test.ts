import { updateCategories } from "../updateCategories";

describe('test update categories function', () => {
    it('should add category', () => {
        expect(updateCategories([], 'Одежда')).toStrictEqual(['Одежда']);
        expect(updateCategories(['Одежда'], 'Электроника')).toStrictEqual(['Одежда', 'Электроника']);
    });

    it('should remove category', () => {
        expect(updateCategories(['Одежда'], 'Одежда')).toStrictEqual([]);
        expect(updateCategories(['Одежда', 'Для дома'], 'Одежда')).toStrictEqual(['Для дома']);
    });
});
