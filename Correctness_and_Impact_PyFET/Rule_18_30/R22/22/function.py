
def f(
  a,
  **kwargs,
) -> A:
    return (
        yield from A(
            very_long_argument_name1=very_long_value_for_the_argument,
            very_long_argument_name2=very_long_value_for_the_argument,
            **kwargs,
        )
    )
    if False:
        yield None