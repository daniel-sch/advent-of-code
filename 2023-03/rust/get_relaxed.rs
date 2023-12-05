use std::cmp::{max, min};
use std::ops::{Bound::*, RangeBounds};

pub trait GetRelaxed<T: ?Sized, R: RangeBounds<i32>> {
    fn get_relaxed(&self, range: R) -> &T;
}

impl<T, R: RangeBounds<i32>> GetRelaxed<[T], R> for Vec<T> {
    fn get_relaxed(&self, range: R) -> &[T] {
        let start = max(
            0,
            match range.start_bound() {
                Unbounded => 0 as i32,
                Included(n) => *n,
                Excluded(n) => *n - 1,
            },
        ) as usize;
        let end = min(
            max(
                0,
                match range.end_bound() {
                    Unbounded => self.len() as i32,
                    Included(n) => *n + 1,
                    Excluded(n) => *n,
                },
            ) as usize,
            self.len(),
        );
        self.get(start..end).unwrap_or_default()
    }
}

impl<R: RangeBounds<i32>> GetRelaxed<str, R> for &str {
    fn get_relaxed(&self, range: R) -> &str {
        let start = max(
            0,
            match range.start_bound() {
                Unbounded => 0 as i32,
                Included(n) => *n,
                Excluded(n) => *n - 1,
            },
        ) as usize;
        let end = min(
            max(
                0,
                match range.end_bound() {
                    Unbounded => self.len() as i32,
                    Included(n) => *n + 1,
                    Excluded(n) => *n,
                },
            ) as usize,
            self.len(),
        );
        self.get(start..end).unwrap_or_default()
    }
}
