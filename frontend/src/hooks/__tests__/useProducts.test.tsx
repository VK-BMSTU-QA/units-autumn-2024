import React from 'react';
import { render, renderHook } from '@testing-library/react';
import '@testing-library/jest-dom';
import { useProducts } from '../useProducts';

describe('useProducts test', () => {
    it('should return correct values', () => {
        const { result } = renderHook(() => useProducts());

        expect(result.current).toMatchSnapshot();
    });
});
