import { updateCategories } from "../updateCategories";

describe('test update categories function', () => {
    it('should add chosen category to categories list if it does not exist in it', () => {
        expect(updateCategories(['Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда','Электроника','Для дома']);
    })

    it('should remove chosen category from categories list if it already exists in it', () => {
        expect(updateCategories(['Для дома','Одежда','Электроника'], 'Для дома')).toStrictEqual(['Одежда', 'Электроника']);
    })
});