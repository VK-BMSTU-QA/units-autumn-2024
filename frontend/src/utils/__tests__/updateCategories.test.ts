import { updateCategories } from '../updateCategories';

describe('test updateCategories function', () => {
    it('should add category', () => {
        expect(updateCategories([], 'Одежда')).toEqual(['Одежда']);
        expect(updateCategories(['Для дома'], 'Одежда')).toEqual([
            'Для дома',
            'Одежда',
        ]);
    });

    it('should remove category', () => {
        expect(updateCategories(['Электроника'], 'Электроника')).toEqual([]);
        expect(updateCategories(['Электроника', 'Одежда'], 'Одежда')).toEqual([
            'Электроника',
        ]);
    });
});
