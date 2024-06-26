/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix.h
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * simple_write is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * simple_write is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#ifndef MQ_POSIX_H_
#Defines MQ_POSIX_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>

#Defines MQ_POSIX_ERROR -1

/**
 * Description:
 *     Print fatal error message and exit with status 1.
 *
 * Arguments:
 *     message - fatal error message
 *
 * Return value:
 *     none
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
void mq_posix_fatal_error(const char * message) __attribute__ ((noreturn));

/**
 * Description:
 *     Creates a new POSIX message queue or opens an existing queue.
 *     Queue is identified by name.
 *
 * Arguments:
 *     mq_name - message queue name
 *     operation_flag - argument specifies flags that control the operation
 *                      of the call
 *
 * Return value:
 *     status - on success returns message queue descriptor for use |
 *              MQ_POSIX_ERROR with error number set to indicate the error:
 *                  EACCES, EACCES, EEXIST, EINVAL, EMFILE, ENAMETOOLONG,
 *                  ENFILE, ENOENT, ENOMEM, ENOSPC
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
mqd_t mq_posix_open(
    const char * name, int operation_flag
) __attribute__((nonnull (1)));

/**
 * Description:
 *     Creates a new POSIX message queue or opens an existing queue.
 *     Queue is identified by name.
 *
 * Arguments:
 *     mq_name - message queue name
 *     operation_flag - argument specifies flags that control the operation
 *                      of the call
 *
 * Return value:
 *     status - on success returns message queue descriptor for use |
 *              MQ_POSIX_ERROR with error number set to indicate the error:
 *                  EACCES, EACCES, EEXIST, EINVAL, EMFILE, ENAMETOOLONG
 *                  ENFILE, ENOENT, ENOMEM, ENOSPC
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
mqd_t mq_posix_open_mode(
    const char * name, int oflag, mode_t mode, struct mq_attr * attr
) __attribute__((nonnull (1, 4)));

/**
 * Description:
 *     Adds the message pointed to by msg_ptr to the messag queue referred
 *     to by the message queue descriptor.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *     message - message for queue
 *     message_length - specifies the length of the message (zero-length
 *                      messages are allowed)
 *     message_priority - specifies the priority of this message
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  EAGAIN, EBADF, EINTR, EINVAL, EMSGSIZE, ETIMEDOUT
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int mq_posix_send(
    mqd_t mq_descriptor, const char * message,
    size_t message_length, unsigned int message_priority
) __attribute__((nonnull (2)));

/**
 * Description:
 *     Receive a message from a message.queue. Removes the oldest message
 *     with the highest priority from the message queue referred to by
 *     the message queue descriptor.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *     message - message for queue
 *     message_length - specifies the length of the message (zero-length
 *                      messages are allowed)
 *     message_priority - specifies the priority of this message
 *
 * Return value:
 *     status - on success returns number of bytes in the received message |
 *              MQ_POSIX_ERROR with error number set to indicate the error:
 *                  EAGAIN, EBADF, EINTR, EINVAL, EMSGSIZE, ETIMEDOUT
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
ssize_t mq_posix_receive(
    mqd_t mq_descriptor, const char * message,
    size_t message_length, unsigned int message_priority
);

/**
 * Description:
 *     Closes the message queue descriptor mqdes. If the calling process
 *     has attached a notification request (see (mq_notify(3)) to this
 *     message queue via mqdes, then this request is removed, and another
 *     process can now attach a notification request.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  EBADF
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */

int mq_posix_close(mqd_t mq_descriptor);

/**
 * Description:
 *     Removes the specified message queue name (message queue name is
 *     removed immediately). The queue itself is destroyed once any other
 *     processes that have the queue open close their descriptors referring
 *     to queue.
 *
 * Arguments:
 *     mq_name - message queue name
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  ENAMETOOLONG, ENOENT, EACCES
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int mq_posix_unlink(const char * mq_name) __attribute__((nonnull (1)));

#ifdef __cplusplus
}
#endif

#endif
