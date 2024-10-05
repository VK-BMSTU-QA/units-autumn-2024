import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(
             <ProductCard
                name="Iphone"
                description="Iphone_desc"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={2}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
        const rendered = render(
            <ProductCard
                name="Iphone"
                description="Iphone_desc"
                price={999}
                priceSymbol="$"
                category="Электроника"
                id={2}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});