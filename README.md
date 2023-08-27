# django-tutorial-4-2

Just a playground for Django v4.2 tutorial app.

## Development

```shell
docker build . -t django-tutorial-4-2
docker run --rm -it -v $PWD:/app -p 8000:8000 django-tutorial-4-2
```

## References

- [Writing your first Django app, part 1 | Django documentation | Django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)
