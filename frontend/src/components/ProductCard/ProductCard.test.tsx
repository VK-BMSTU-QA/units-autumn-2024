import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { getPrice } from '../../utils';

jest.mock('../../utils');

afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    it('should render correctly', () => {
        jest.mocked(getPrice).mockReturnValue('999 $')

        const rendered = render(
            <ProductCard 
                id={1}
                name='IPhone 14 Pro' 
                description='Latest iphone, buy it now'
                price={999}
                priceSymbol='$'
                category='Электроника'
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should not add product img', () => {
        jest.mocked(getPrice).mockReturnValue('999 $')

        const rendered = render(
            <ProductCard 
                id={1}
                name='IPhone 14 Pro' 
                description='Latest iphone, buy it now'
                price={999}
                priceSymbol='$'
                category='Электроника'
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(rendered.findAllByAltText('IPhone 14 Pro')).toStrictEqual(Promise.resolve({}));
    });

    it('should add product img', () => {
        jest.mocked(getPrice).mockReturnValue('999 $')

        const rendered = render(
            <ProductCard 
                id={1}
                name='IPhone 14 Pro' 
                description='Latest iphone, buy it now'
                price={999}
                priceSymbol='$'
                category='Электроника'
                imgUrl='/iphone.png'
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(rendered.getByAltText('IPhone 14 Pro')).toHaveClass('product-card__image');
    });
});