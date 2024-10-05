import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

jest.mock('../../utils');

const fixtureProduct: Product = {
    id: 1,
    name: 'IPhone 14 Pro' ,
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category:'Электроника',
};

afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    beforeEach(() => {
        jest.mocked(getPrice).mockReturnValue('999 $');
    });

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render name', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(rendered.getByText('IPhone 14 Pro')).toBeInTheDocument();
    });

    it('should render description', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(rendered.getByText('Latest iphone, buy it now')).toBeInTheDocument();
    });

    it('should render category', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(rendered.getByText('Электроника')).toBeInTheDocument();
    });

    it('should render price', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(getPrice).toBeCalledTimes(1);
        expect(rendered.getByText('999 $')).toBeInTheDocument();
    });

    it('should not add product img', () => {
        const rendered = render(<ProductCard {...fixtureProduct} />);

        expect(rendered.findAllByAltText('IPhone 14 Pro')).resolves.toStrictEqual({});
    });

    it('should add product img', () => {
        const rendered = render(<ProductCard {...fixtureProduct} imgUrl='/iphone.png' />);

        expect(rendered.getByAltText('IPhone 14 Pro')).toBeInTheDocument();
    });
});
