import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);
jest.mock('../../utils');

describe('Products test', () => {
    it('should mock get price function', () => {
        jest.mocked(getPrice).mockReturnValue('100 RK6');

        render(
            <ProductCard
                id={1}
                name={'Andrew'}
                description={'RK6 developer'}
                price={100}
                category={'Электроника'}
            />
        );

        expect(getPrice).lastReturnedWith('100 RK6');
    });
    it('should add img by given url', () => {
        const rendered = render(
            <ProductCard
                id={1}
                name={'Andrew'}
                description={'RK6 developer'}
                price={100}
                category={'Электроника'}
                imgUrl={'public/iphone.png'}
            />
        );

        expect(rendered.getByAltText('Andrew')).toHaveClass(
            'product-card__image'
        );
    });
    it('should not add img', () => {
        const rendered = render(
            <ProductCard
                id={12}
                name={'Aleshka'}
                description={'BMSTU Student'}
                price={0}
                priceSymbol={'₽'}
                category={'Для дома'}
            />
        );

        expect(rendered.queryAllByAltText('Andrew').length).toEqual(0);
    });
});
