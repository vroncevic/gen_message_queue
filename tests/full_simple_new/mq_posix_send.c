/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * mq_posix_send.c
 * Copyright (C) 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
 *
 * full_simple_new is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * full_simple_new is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License along
 * with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#include "mq_posix.h"

/**
 * Description:
 *     Adds the message pointed to by msg_ptr to the messag queue referred
 *     to by the message queue descriptor.
 *
 * Arguments:
 *     mq_descriptor - message queue descriptor
 *     message - message for queue (if the message queue is already full
 *               (i.e., the number of) messages on the queue equals the
 *               queue's mq_maxmsg attribute) then, by default, mq_send()
 *               blocks until sufficient space becomes available to allow
 *               the message to be queued, or until the call is interrupted
 *               by a signal handler if the O_NONBLOCK flag is enabled for
 *               the message queue description, then the call instead fails
 *               immediately with the error EAGAIN
 *     message_length - specifies the length of the message (zero-length
 *                      messages are allowed)
 *     message_priority - specifies the priority of this message Messages
 *                        are placed on the queue in decreasing order of
 *                        priority, with newer messages of the same priority
 *                        being placed after older messages with the same
 *                        priority
 *
 * Return value:
 *     status - on success returns 0 | MQ_POSIX_ERROR with error number
 *              set to indicate the error:
 *                  EAGAIN (the queue was full, and the O_NONBLOCK flag
 *                          was set for the message queue description
 *                          referred to by mqdes)
 *                  EBADF (the descriptor specified in mqdes was invalid
 *                         or not opened for writing)
 *                  EINTR (the call was interrupted by a signal handler)
 *                  EINVAL (the call would have blocked, and abs_timeout
 *                          was invalid, either because tv_sec was less
 *                          than zero, or because tv_nsec was less than
 *                          zero or greater than 1000 million)
 *                  EMSGSIZE (msg_len was greater than the mq_msgsize
 *                            attribute of the message queue)
 *                  ETIMEDOUT (the call timed out before a message could be
 *                             transferred)
 *
 * Standards:
 *     POSIX.1-2001, POSIX.1-2008
 */
int mq_posix_send(
    mqd_t mq_descriptor, const char * message,
    size_t message_length, unsigned int message_priority
)
{
    int status;

    if (
        mq_descriptor != MQ_POSIX_ERROR &&
        message != NULL &&
        message_length >= 0
    )
    {
        status = mq_send(
            mq_descriptor, message, message_length, message_priority
        );
    }
    else
    {
        status = MQ_POSIX_ERROR;
    }

    return status;
}

