import { render } from '@testing-library/react';
import { ProductCard } from './ProductCard';

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                id={1}
                name="IPhone 14 Pro"
                description="Latest iphone buy it now"
                price={999}
                priceSymbol="$"
                category="Электроника"
                imgUrl="/iphone.png"
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without imageUrl', () => {
        const rendered = render(
            <ProductCard
                id={2}
                name="Костюм гуся"
                description="Запускаем гуся работяги"
                price={1000}
                priceSymbol="₽"
                category="Одежда"
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
