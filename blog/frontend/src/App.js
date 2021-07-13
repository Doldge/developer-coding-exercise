import './App.css';
import React from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            loaded: false,
            postList: {},
            activePost: null
        };
    }

    refetchList() {
      fetch("/posts/", {
        headers: {
          "Content-Type": "application/json"
        }
      })
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              postList: result,
              loaded: true
            })
          },
          (error) => {
            console.log('fetch failed!');
            console.log(error);
          });
    }

    componentDidMount() {
      this.refetchList();
    }

    async onPostClick(item) {
      if (item != undefined) {
        fetch(
          "/posts/".concat(item.slug).concat('/'), {
            headers: {
              "Content-Type": "application/json"
            }
        })
          .then(res => res.json())
          .then(
            (result) => {
              this.setState({
                activePost: result,
              })
            },
            (error) => {
              console.log('failed to load post!');
              console.log(error);
            });
      } else {
        this.setState({
          activePost: item
        });
      }
    }

    renderPost() {
      const {title, author, content} = this.state.activePost;
      return (
        <div className="post">
          <h1>{title}</h1>
          <h4>Author: {author}</h4>
          <ReactMarkdown rehypePlugins={[rehypeRaw]}>{content}</ReactMarkdown>
          <btn onClick={() => this.onPostClick(undefined)}>Back</btn>
        </div>
      );
    }

    renderList() {
      const { loaded, postList } = this.state;
      if (! loaded ) {
        return (<div>Loading...</div>);
      } else {
        return (
          <ul>
            {postList.map(item => (
              <li>
                <btn onClick={() => this.onPostClick(item)}>{item.title}</btn>
              </li>
            ))}
          </ul>
        );
      }
    }

    render() {
      const { activePost } = this.state;
      if (activePost == undefined) {
        return (
          <div className="App">
            {this.renderList()}
          </div>
        );
      } else {
        return (
          <div className="App">
            {this.renderPost()}
          </div>
        );
      }
    }
}

export default App;
