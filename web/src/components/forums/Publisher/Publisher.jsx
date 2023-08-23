import React, {useState} from 'react';
import {Box, Button, DialogContent, DialogTitle, IconButton, Input, Switch, Typography} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import {useStyles} from './Publisher.styles';
import RichTextEditor from '../Editor/RichTextEditor';
import {useSnackbar} from 'notistack';

export default function Publisher({
  mode = 'post',
  setOpen,
  onClose,
  handlePublish,
  initalTitle = '',
  initialContent = null,
  visibleToStudents = true,
  anonymous = false,
}) {
  // MUI theme-based css styles
  const classes = useStyles();
  // Form Data
  const [title, setTitle] = useState(initalTitle);
  const [content, setContent] = useState(initialContent ? initialContent : {});
  const [isVisibleToStudents, setIsVisisbleToStudents] = useState(visibleToStudents);
  const [isAnonymous, setIsAnonymous] = useState(anonymous);
  const {enqueueSnackbar} = useSnackbar();

  const isPost = mode === 'post';

  const validatePost = () => {
    if (title && content) {
      handlePublish({
        title: title,
        content: content,
        visible_to_students: isVisibleToStudents,
        anonymous: isAnonymous,
      });
      if (onClose) onClose();
    } else if (content && !isPost) {
      handlePublish({
        content: content,
        anonymous: isAnonymous,
        visible_to_students: isVisibleToStudents,
      });
      if (onClose) onClose();
    } else {
      enqueueSnackbar('Add content!', {variant: 'warning'});
    }
  };

  return (
    <Box className={classes.publisherContainer}>
      {isPost &&
        <DialogTitle className={classes.titleContainer}>
          <Box display="flex" alignItems="center">
            <Box flexGrow={1}>{isPost ? 'Create A New Post' : 'Create A New Comment'}</Box>
            <IconButton onClick={() => setOpen(false)}>
              <CloseIcon/>
            </IconButton>
          </Box>
        </DialogTitle>
      }
      <DialogContent sx={{padding: 0}}>
        {isPost &&
          <Input inputProps={{className: classes.inputTitle}} disableUnderline={true} fullWidth
            value={title} onChange={(e) => setTitle(e.target.value)} placeholder={'Put Title Here'}/>
        }
        {isPost ?
          <RichTextEditor setContent={setContent} content={initialContent} /> :
          <RichTextEditor setContent={setContent} content={initialContent} setOpen={setOpen}/>
        }
        <Box display="flex" alignItems="center" justifyContent="flex-start" gap="20px" padding="0px 10px">
          <div className={classes.switchContainer}>
            <Typography>Visible to Students?</Typography>
            <Switch checked={isVisibleToStudents} onChange={() => setIsVisisbleToStudents(!isVisibleToStudents)}/>
          </div>
          <div className={classes.switchContainer}>
            <Typography>Anonymous?</Typography>
            <Switch checked={isAnonymous} onChange={() => setIsAnonymous(!isAnonymous)}/>
          </div>
        </Box>
      </DialogContent>
      <Button
        variant={'contained'}
        className={classes.submit}
        onClick={validatePost}
      >
        {isPost ? 'Post' : 'Comment'}
      </Button>
    </Box>
  );
}
