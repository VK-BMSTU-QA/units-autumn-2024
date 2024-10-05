import {render, screen} from '@testing-library/react';
import {ProductCard} from '../ProductCard';
import {getPrice} from '../../utils';
import '@testing-library/jest-dom';

jest.mock('../../utils', () => ({
    getPrice: jest.fn(),
}));

describe('ProductCard Component', () => {
    const product = {
        id: 1,
        name: 'IPhone 14 Pro',
        description: 'Latest iPhone model',
        price: 999,
        category: 'Электроника',
        imgUrl: '/iphone.png',
    };

    beforeEach(() => {
        (getPrice as jest.Mock).mockImplementation((price, symbol) => `${price} ${symbol}`);
    });

    it('should render the product details correctly', () => {
        render(<ProductCard id={1}
                            name={'IPhone 14 Pro'}
                            description={'Latest iPhone model'}
                            price={999}
                            priceSymbol={'$'}
                            category={'Электроника'}
                            imgUrl={'/iphone.png'}/>);
        expect(screen.getByText('IPhone 14 Pro')).toBeInTheDocument();
        expect(screen.getByText('Latest iPhone model')).toBeInTheDocument();
        expect(screen.getByText('Электроника')).toBeInTheDocument();
        expect(screen.getByText('999 $')).toBeInTheDocument(); // price formatted by getPrice
    });

    it('should render the product image when imgUrl is provided', () => {
        render(<ProductCard id={1}
                            name={'IPhone 14 Pro'}
                            description={'Latest iPhone model'}
                            price={999}
                            priceSymbol={'$'}
                            category={'Электроника'}
                            imgUrl={'/iphone.png'}/>);
        const image = screen.getByAltText('IPhone 14 Pro');
        expect(image).toBeInTheDocument();
        expect(image).toHaveAttribute('src', '/iphone.png');
    });

    it('should not render the product image when imgUrl is missing', () => {

        render(<ProductCard id={1}
                            name={'IPhone 14 Pro'}
                            description={'Latest iPhone model'}
                            price={999}
                            priceSymbol={'$'}
                            category={'Электроника'}
        />);
        expect(screen.queryByAltText('IPhone 14 Pro')).not.toBeInTheDocument();
    });

});
