import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../utils');

afterEach(jest.clearAllMocks);

describe('ProductCard test', () => {
    it('should render correctly', () => {
        jest.mocked(getPrice).mockReturnValue('999 шекелей');

        const product: Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
            imgUrl: '/iphone.png',
        }

        expect(getPrice).toHaveBeenCalledTimes(0);

        const rendered = render(
            <ProductCard
                id = {product.id}
                name={product.name}
                description={product.description}
                price={product.price}
                priceSymbol={product.priceSymbol}
                category={product.category}
                imgUrl={product.imgUrl}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(getPrice).toHaveBeenCalledTimes(1);
    });
    
    it('should not render image if imgUrl is not provided', () => {
        const product: Product = {
            id: 1,
            name: 'IPhone 14 Pro',
            description: 'Latest iphone, buy it now',
            price: 999,
            priceSymbol: '$',
            category: 'Электроника',
        }

        jest.mocked(getPrice).mockReturnValue('999 шекелей');

        const rendered = render(
            <ProductCard
                id = {product.id}
                name={product.name}
                description={product.description}
                price={product.price}
                priceSymbol={product.priceSymbol}
                category={product.category}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.queryByAltText(product.name)).toBeNull();
    });
});
