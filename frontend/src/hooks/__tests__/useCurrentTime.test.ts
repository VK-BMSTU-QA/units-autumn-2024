import { useEffect, useState } from 'react';
import { useCurrentTime } from '../useCurrentTime';
import {renderHook, act} from '@testing-library/react';

describe('test use current time function', () => {
    beforeAll(() => {
        jest.useFakeTimers().setSystemTime(new Date('2001-09-11 00:00:00'));
    });

    test('должно вернуть текущее время', () => {
        const { result } = renderHook(useCurrentTime);
        expect(result.current).toEqual('00:00:00');
        act(() => jest.advanceTimersByTime(2000));
        expect(result.current).toEqual('00:00:02');
    });
});
