import { renderHook } from '@testing-library/react';
import { useCurrentTime } from '../useCurrentTime';

describe('useCurrentTime test', () => {
    it('should match the pattern', () => {
        const { result } = renderHook(useCurrentTime);
        expect(result.current).toMatch(/\d{2}:\d{2}:\d{2}/);
    });
});
