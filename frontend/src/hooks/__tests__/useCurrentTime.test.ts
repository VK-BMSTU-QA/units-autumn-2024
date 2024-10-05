import { useCurrentTime } from '../useCurrentTime';
import { renderHook } from '@testing-library/react';

describe('test use current time function', () => {
    it('should return mocked time', () => {
        const mockedDateData = '2024-10-05T09:33:21'
        
        const mockDateReturn = jest
            .spyOn(Date.prototype, 'toLocaleTimeString')
            .mockReturnValue(mockedDateData);

        const { result } = renderHook(useCurrentTime);

        expect(mockDateReturn).toBeCalledTimes(1);
        expect(result.current).toBe(mockedDateData);
    });
});