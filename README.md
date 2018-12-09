# placecamera

I was passionate about photography, now I'm passionate about web development. placecamera is a service (in form of website), where you pass width and height to the website and it generates and returns an image of same dimension. Somewhat in this fashion.

```sh
http://localhost:3698/1920/1080
```

Other parameters are available, and more coming. See [Usage](#Usage).

placecamera is intended to be used by front-end developers who need images to test their design and spend time hunting images. Your journey ends here. 

placecamera was [initially written][php version] (partially complete) in PHP, now I'm porting it to Python, with Django as a backend.

**placecamera** is inspired by *placeholder.com*

## Usage

To be updated..

## Contribute

If you have any idea, or you feel something is buggy, or just have any question, feel free to [open an issue][new issue page]. 

If you are a developer, there are a lot work to be done. See [Design](#Design) section. Also see [contribution guidelines](./CONTRIBUTING.md).

## Development

If you are developing locally, follow these instruction.

To be updated..

### Design

- [ ] Produce square image if only one param is passed
- [ ] If two params are passed take first as width, other as height
<!-- - [ ] Use PNG (do we need others?) -->
<!-- - [ ] Add support for text | really? on camera? -->
- [ ] Add support for BG and FG color

### TODOs

- [ ] Write unit tests
- [ ] Write documentation, generate using Sphinx

## License

This project is licensed under MIT. See [LICENSE.md](./LICENSE.md) for full license.

[php version]: https://github.com/santosh/placecamera/tree/555cfd
[new issue page]: https://github.com/santosh/placecamera/issues/new